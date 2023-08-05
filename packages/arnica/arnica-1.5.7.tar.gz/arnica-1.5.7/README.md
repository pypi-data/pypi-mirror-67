# ARNICA 


![logo_arnica](http://cerfacs.fr/coop/whatwedo/logo_arnica.gif)
ARNICA stands for "All Recurrent No-brainers In Cerfacs Applications". 
We keep there all the simple little things we regularly need.

*It is available on [pipy](https://pypi.org/project/arnica/), 
documentation is on [readtthedocs](https://arnica.readthedocs.io/en/latest/), sources are mirrored on [gitlab.com](https://gitlab.com/cerfacs/ms_thermo)*

We still have to write a proper introduction. sorry for that...


For example a cartesian-to-cylindrical conversion around x-axis, with a specific convention 

```python
def rtheta2yz(rrr, theta):
    """ return yz fror rtheta ,
    theta in  radians measure of ange in the yz plane,
    - range -pi/pi
    - 0 on the y+ axis (z=0, y>0)
    spanning -pi to pi

                        0pi=0deg
                      Y
                      ^
                      |
                      |
    -0.5pi=-90deg     o------>Z   0.5pi=90deg

    """
    yyy = rrr * np.cos(theta)
    zzz = rrr * np.sin(theta)
    return yyy, zzz
```

Ok trivial, but I did mention it was a no-brainer no?
A no-brainer, but with a constant convention and unitary testing to be sure nobody will change it.


Browse into the SPHINX documentation to see the content, such as RBF cloud to cloud interpolation, and much more funny functions.


# Installation

Arnica can be installed directly in your Python 3 environnement by running the command:

```
pip install arnica
```

This command will install Arnica and all its dependencies (if needed). Once this step is over you can use arnica as a Python module in a script:

```python
import arnica
```
# Motivation

Having these bits in a single repository adds the following values:

- Unitary testing.
- linting.
- Automatic documentation.
- Can be used by others in Cerfacs.

In Arnica, useful features related to Computational Fluid Dynamics (CFD) are implemented, namely:

  1. *CFD related tools* aiming to be used together with the Reactive software suite [AVBP](http://www.cerfacs.fr/avbp7x/).
  2. *CFD related bare functionnalities* such as ParaView-readable XDMF writers from Numpy arrays, axi-symetric shell generators, 2D finite differences solvers, _etc._
  

# License

CeCILL-B FREE SOFTWARE LICENSE AGREEMENT
