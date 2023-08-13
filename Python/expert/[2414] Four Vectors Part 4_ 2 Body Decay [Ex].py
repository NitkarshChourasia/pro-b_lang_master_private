"""
####  Four Vectors Part 4: 2 Body Decay  ####

In this challenge, we make use of the FourVector class we created in the first three challenges of this series (part 1, part 2, and part 3). We will turn to a (simplified) two-body decay, i.e. one particle decays into two daughter particles. This is a typical situation e.g. in particle physics experiments.
Please extend the FourVector class by a method GetInvariantMass which accepts as parameters a list of 4-vectors (which, in this challenge, will contain exactly one element) and returns the invariant mass of the system of 4-vectors, i.e. the sum of the 4-vector whose instance the method is called upon and the 4-vector(s) from the list. Please see the wiki link in the ressources for details on the invariant mass. It is simply the length of the 4-vector sum.
Furthermore, please provide a function (outside the class FourVector) find_particle which accepts two FourVector instances as input. Based on the invariant mass of these (which makes use of the method mentioned in the previous section), return the name of the particle which decayed into the two daughters which are represented by the two 4-vectors. We will only cover four particles here: the Higgs boson (mass 125.1 GeV), the Sigma+ baryon (mass 1.18937 GeV), the J/Psi meson (mass 3.0969 GeV), and the charged pion (pi meson, mass 0.139570 GeV). Please note that we are using "particle physics units" for mass here, i.e. units where the speed of light and Planck's constant are set to 1.
Names to be returned are "Higgs", "J/Psi", "Sigma+" and "Pi+", respectively.
Please note that masses may not match exactly the values mentioned above, please allow some room for error (see note below).


[Examples]

___
fv1 = FourVector([62.55, 7.522814397445341, 50.95236974441615, -35.448674862543086])
fv2 = FourVector([62.55, -7.522814397445341, -50.95236974441615, 35.448674862543086])
find_particle(fv1, fv2) ➞ "Higgs"
_____



[Notes]

In particle physics experiments, various detector components are responsible for measuring the particle's energy and momenta as precisely as possible. Based on these, the particle type and therefore it's rest mass and therefore the complete energy-momentum-four vector can (in principle) be reconstructed. By calculating the invariant mass of several four vectors, searches for mother particles that decayed into the detected particles are possible. In reality, this is much more complicated and many sources of errors are present. To take that into account a bit, the test data contains cases where the mass of the mother particle does match only approximately the values mentioned above.
Details on particle properties like mass and decay modes are provided by the particle data group, see Resources.


[classes] [math] [physics] 



-------------------------------------------------------------------
[Resources]
_________
Invariant Mass
https://en.wikipedia.org/wiki/Invariant_mass
Is the portion of the total mass of an object or system of objects that is independent of the overall motion of the system. More precisely, it is a characteristic of t …
_________
_________
Particle Physics
https://pdg.lbl.gov/
Particle Physics booklet 2018 available for mobile or direct download.
_________

"""
#Your code should go here:

