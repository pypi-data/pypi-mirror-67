from distfit.distfit import distfit as fitdist


__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.0'

# module level doc-string
__doc__ = """
fitdist
=====================================================================

Description
-----------
Probability density fitting and hypothesis testing.
Computes best fit to the input emperical distribution for 89 theoretical
distributions using the Sum of Squared errors (SSE) estimates.

Example
-------
>>> from fitdist import fitdist
>>>
>>> X = np.random.normal(0, 2, 1000)
>>> y = [-8,-6,0,1,2,3,4,5,6]
>>>
>>> dist = fitdist()
>>> dist.fit_transform(X)
>>> dist.plot()
>>>
>>> # Make prediction
>>> dist.predict(y)
>>> dist.plot()

References
----------
https://github.com/erdogant/distfit

"""
