from random import randrange

STRENGTH = 10
DEFENSE = 10

energy = 25

attack_force = randrange(20)
attack_intensity = randrange(5)

if attack_force > DEFENSE:
    energy = energy - attack_intensity
    print("Attack received ( %i ): Energy = %i" % (attack_force, energy))
else:
    print("Attack ( %i ) blocked!" % attack_force)

