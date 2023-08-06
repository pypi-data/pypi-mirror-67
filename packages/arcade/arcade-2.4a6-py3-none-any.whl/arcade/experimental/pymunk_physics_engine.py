"""
Pymunk Physics Engine
"""

import pymunk
import math
from typing import Callable
from typing import List
from typing import Dict
from typing import Optional
from arcade import Sprite
from arcade import SpriteList

class PymunkPhysicsObject:
    def __init__(self,
                 body: pymunk.Body = None,
                 shape: pymunk.Shape = None):
        self.body: pymunk.Body = body
        self.shape: pymunk.Shape = shape


class PymunkPhysicsEngine:
    """
    Pymunk Physics Engine
    """

    DYNAMIC = pymunk.Body.DYNAMIC
    STATIC = pymunk.Body.STATIC
    KINEMATIC = pymunk.Body.KINEMATIC
    MOMENT_INF = pymunk.inf

    def __init__(self, gravity=(0, 0), damping: float = 1.0):
        # -- Pymunk
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.space.damping = damping
        self.collision_types: List[str] = []
        self.sprites: Dict[Sprite, PymunkPhysicsObject] = {}

    def add_sprite(self,
                   sprite: Sprite,
                   mass: float = 1,
                   friction: float = 0.2,
                   elasticity: Optional[float] = None,
                   moment=None,
                   body_type=DYNAMIC,
                   damping=None,
                   gravity=None,
                   max_velocity=None,
                   max_horizontal_velocity=None,
                   max_vertical_velocity=None,
                   radius: float = 0,
                   collision_type: str = "default",
                   ):
        """ Add a sprite to the physics engine. """

        if sprite in self.sprites:
            print("Sprite already in space.")

        if collision_type not in self.collision_types:
            self.collision_types.append(collision_type)

        collision_type_id = self.collision_types.index(collision_type)

        if moment is None:
            moment = pymunk.moment_for_box(mass, (sprite.width, sprite.height))

        body = pymunk.Body(mass, moment, body_type=body_type)
        body.position = pymunk.Vec2d(sprite.center_x, sprite.center_y)

        def velocity_callback(my_body, my_gravity, my_damping, dt):
            """ Used for custom damping, gravity, and max_velocity. """
            if damping is not None:

                adj_damping = ((damping * 100) / 100) ** dt
                # print(damping, my_damping, adj_damping)
                my_damping = adj_damping
            if gravity is not None:
                my_gravity = gravity

            pymunk.Body.update_velocity(my_body, my_gravity, my_damping, dt)

            if max_velocity:
                velocity = my_body.velocity.length
                if velocity > max_velocity:
                    scale = max_velocity / velocity
                    my_body.velocity = my_body.velocity * scale

            if max_horizontal_velocity:
                velocity = my_body.velocity.x
                if abs(velocity) > max_horizontal_velocity:
                    velocity = max_horizontal_velocity * math.copysign(1, velocity)
                    my_body.velocity = pymunk.Vec2d(velocity, my_body.velocity.y)

            if max_vertical_velocity:
                velocity = my_body.velocity[1]
                if abs(velocity) > max_vertical_velocity:
                    velocity = max_horizontal_velocity * math.copysign(1, velocity)
                    my_body.velocity = pymunk.Vec2d(my_body.velocity.x, velocity)

        body.velocity_func = velocity_callback

        poly = sprite.get_hit_box()

        scaled_poly = [[x * sprite.scale for x in z] for z in poly]

        shape = pymunk.Poly(body, scaled_poly, radius=radius)

        if collision_type:
            shape.collision_type = collision_type_id
        if elasticity is not None:
            shape.elasticity = elasticity
        shape.friction = friction

        physics_object = PymunkPhysicsObject(body, shape)
        self.sprites[sprite] = physics_object

        self.space.add(body, shape)
        sprite.register_physics_engine(self)

    def add_sprite_list(self,
                        sprite_list,
                        mass: float = 1,
                        friction: float = 0.2,
                        elasticity: Optional[float] = None,
                        moment=None,
                        body_type=DYNAMIC,
                        collision_type=None
                        ):
        """ Add all sprites in a sprite list to the physics engine. """

        for sprite in sprite_list:
            self.add_sprite(sprite, mass, friction, elasticity, moment, body_type, collision_type=collision_type)

    def remove_sprite(self, sprite: Sprite):
        """ Remove a sprite from the physics engine. """
        physics_object = self.sprites[sprite]
        self.space.remove(physics_object.body)
        self.space.remove(physics_object.shape)

    def get_sprite_for_shape(self, shape) -> Optional[Sprite]:
        """ Given a shape, what sprite is associated with it? """
        for sprite in self.sprites:
            if self.sprites[sprite].shape is shape:
                return sprite
        return None

    def add_collision_handler(self,
                              first_type: str,
                              second_type: str,
                              begin_handler: Callable = None,
                              pre_handler: Callable = None,
                              post_handler: Callable = None,
                              separate_handler: Callable = None):
        """ Add code to handle collisions between objects. """
        if first_type not in self.collision_types:
            self.collision_types.append(first_type)
        first_type_id = self.collision_types.index(first_type)

        if second_type not in self.collision_types:
            self.collision_types.append(second_type)
        second_type_id = self.collision_types.index(second_type)

        h = self.space.add_collision_handler(first_type_id, second_type_id)
        if begin_handler:
            h.begin = begin_handler
        if post_handler:
            h.post_solve = post_handler
        if pre_handler:
            h.pre_solve = pre_handler
        if separate_handler:
            h.separate = separate_handler

    def resync_sprites(self):
        """ Set visual sprites to be the same location as physics engine sprites. """
        for sprite in self.sprites:
            physics_object = self.sprites[sprite]
            sprite.center_x = physics_object.body.position.x
            sprite.center_y = physics_object.body.position.y
            sprite.angle = math.degrees(physics_object.body.angle)

    def step(self, delta_time: float = 1 / 60.0):
        """ Tell the physics engine to perform calculations. """
        # Update physics
        # Use a constant time step, don't use delta_time
        # See "Game loop / moving time forward"
        # http://www.pymunk.org/en/latest/overview.html#game-loop-moving-time-forward
        self.space.step(delta_time)
        self.resync_sprites()

    def get_physics_object(self, sprite: Sprite) -> PymunkPhysicsObject:
        """ Get the shape/body for a sprite. """
        return self.sprites[sprite]

    def apply_force(self, sprite, force):
        """ Apply force to a Sprite. """
        physics_object = self.sprites[sprite]
        physics_object.body.apply_force_at_local_point(force, (0, 0))

    def set_velocity(self, sprite, velocity):
        """ Apply force to a Sprite. """
        physics_object = self.sprites[sprite]
        cv = physics_object.body.velocity
        new_cv = (velocity, cv[1])
        physics_object.body.velocity = new_cv

    def set_friction(self, sprite, friction):
        """ Apply force to a Sprite. """
        physics_object = self.sprites[sprite]
        physics_object.shape.friction = friction

    def apply_opposite_running_force(self, sprite: Sprite):
        """
        If a sprite goes left while on top of a dynamic sprite, that sprite
        should get pushed to the right.
        """
        grounding = self.check_grounding(sprite)
        body = self.get_physics_object(sprite).body
        if body.force[0] and grounding and grounding['body']:
            grounding['body'].apply_force_at_world_point((-body.force[0], 0), grounding['position'])

    def check_grounding(self, sprite: Sprite):
        """ See if the player is on the ground. Used to see if we can jump. """
        grounding = {
            'normal': pymunk.Vec2d.zero(),
            'penetration': pymunk.Vec2d.zero(),
            'impulse': pymunk.Vec2d.zero(),
            'position': pymunk.Vec2d.zero(),
            'body': None
        }

        def f(arbiter):
            n = -arbiter.contact_point_set.normal
            if n.y > grounding['normal'].y:
                grounding['normal'] = n
                grounding['penetration'] = -arbiter.contact_point_set.points[0].distance
                grounding['body'] = arbiter.shapes[1].body
                grounding['impulse'] = arbiter.total_impulse
                grounding['position'] = arbiter.contact_point_set.points[0].point_b

        physics_object = self.sprites[sprite]
        physics_object.body.each_arbiter(f)

        return grounding