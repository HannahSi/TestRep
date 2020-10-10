from aguaclara.core.units import unit_registry as u

gravity = u.gravity

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import aguaclara.core.utility as ut

WATER_DENSITY_TABLE = [(273.15, 278.15, 283.15, 293.15, 303.15, 313.15,
                        323.15, 333.15, 343.15, 353.15, 363.15, 373.15
                        ), (999.9, 1000, 999.7, 998.2, 995.7, 992.2,
                            988.1, 983.2, 977.8, 971.8, 965.3, 958.4
                            )
                       ]
@ut.list_handler()
def viscosity_dynamic(temp):
    """Return the dynamic viscosity of water at a given temperature.

    :param temp: temperature of water
    :type temp: u.degK

    :return: dynamic viscosity of water
    :rtype: u.kg/(u.m*u.s)
    """
    return 2.414*(10**-5)*u.kg/(u.m*u.s) * 10**(247.8*u.degK / (temp - 140*u.degK))

@ut.list_handler()
def density_water(temp):
    """Return the density of water at a given temperature.

    :param temp: temperature of water
    :type temp: u.degK

    :return: density of water
    :rtype: u.kg/u.m**3
    """
    rhointerpolated = interpolate.CubicSpline(WATER_DENSITY_TABLE[0],
                                              WATER_DENSITY_TABLE[1])
    temp = temp.to(u.degK).magnitude
    return rhointerpolated(temp).item() * u.kg/u.m**3

@ut.list_handler()
def viscosity_kinematic(temp):
    """Return the kinematic viscosity of water at a given temperature.

    :param temp: temperature of water
    :type temp: u.degK

    :return: kinematic viscosity of water
    :rtype: u.m**2/u.s
    """
    return (viscosity_dynamic(temp) / density_water(temp))

@ut.list_handler()
def Re_Ergun(ApproachVel, DiamParticle, Temperature, Porosity):
    """Return the Reynolds number for flow through porous media.

    :param ApproachVel: approach velocity or superficial fluid velocity
    :type ApproachVel: u.m/u.s
    :param DiamParticle: particle diameter
    :type DiamParticle: u.m
    :param Temperature: temperature of porous medium
    :type Temperature: u.degK
    :param Porosity: porosity of porous medium
    :type Porosity: u.dimensionless

    :return: Reynolds number for flow through porous media
    :rtype: u.dimensionless
    """
    return (ApproachVel * DiamParticle /
            (viscosity_kinematic(Temperature) * (1 - Porosity)))


@ut.list_handler()
def f_Ergun(ApproachVel, DiamParticle, Temperature, Porosity):
    """Return the friction factor for flow through porous media.

    :param ApproachVel: superficial fluid velocity (VelSuperficial?)
    :type ApproachVel: u.m/u.s
    :param DiamParticle: particle diameter (DiamParticle?)
    :type DiamParticle: u.m
    :param Temperature: temperature of porous medium
    :type Temperature: u.degK
    :param Porosity: porosity of porous medium
    :type Porosity: u.dimensionless

    :return: friction factor for flow through porous media
    :rtype: u.dimensionless
    """
    return (300 / Re_Ergun(ApproachVel, DiamParticle, Temperature, Porosity)
            + 3.5 * u.dimensionless)


@ut.list_handler()
def hf_Ergun(ApproachVel, DiamParticle, Temperature, Porosity, L):
    """Return the frictional head loss for flow through porous media.

    :param ApproachVel: superficial fluid velocity (VelSuperficial?)
    :type ApproachVel: u.m/u.s
    :param DiamParticle: particle diameter (DiamParticle?)
    :type DiamParticle: u.m
    :param Temperature: temperature of porous medium
    :type Temperature: u.degK
    :param Porosity: porosity of porous medium
    :type Porosity: u.dimensionless
    :param L: length of pipe or duct (Length?)
    :type L: u.m

    :return: frictional head loss for flow through porous media
    :rtype: u.m
    """
    return (f_Ergun(ApproachVel, DiamParticle, Temperature, Porosity)
            * L / DiamParticle * ApproachVel**2 / (2*gravity) * (1-Porosity)
            / Porosity**3).to(u.m)



@ut.list_handler()
def G_CS_Ergun(ApproachVel, DiamParticle, Temperature, Porosity):
    """Camp Stein velocity gradient for flow through porous media.

    :param ApproachVel: superficial fluid velocity (VelSuperficial?)
    :type ApproachVel: u.m/u.s
    :param DiamParticle: particle diameter (DiamParticle?)
    :type DiamParticle: u.m
    :param Temperature: temperature of porous medium
    :type Temperature: u.degK
    :param Porosity: porosity of porous medium
    :type Porosity: u.dimensionless

    :return: ...
    :rtype:
    """
    return np.sqrt(f_Ergun(ApproachVel, DiamParticle, Temperature, Porosity)
                   * ApproachVel**3 * (1-Porosity)
                   / (2 * viscosity_kinematic(Temperature) * DiamParticle
                   * Porosity**4)).to(u.Hz)

approach_velocity = list(np.arange(1, 100, 0.1))
friction = f_Ergun(approach_velocity * u.m/u.s, 1 * 10 **-6 * u.m, 20 * u.degC, 0.1)
plt.xlabel("Approach Velocity (m/s)", fontsize=14)
plt.ylabel("Friction Factor", fontsize=14)
plt.title("Friction of Flow through Porous Media", fontsize=14)
plt.plot(approach_velocity, friction)
plt.savefig("Va vs F.png")
