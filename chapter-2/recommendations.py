#!/usr/bin/python

import sys, os
from math import sqrt

critics={'Lisa Rose':{'Lady in the Water':2.5, 'Snake on a Plane': 3.5,
    'Just My Luck':3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
    'The Night Listener': 3.0},
    'Gene Seymour':{'Lady in the Water':3.0, 'Snake on a Plane': 3.5,
    'Just My Luck':1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
    'You, Me and Dupree': 3.5},
    'Michael Philips':{'Lady in the Water':2.5,  'Snake on a Plane': 3.0,
    'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig':{'Snake on a Plane': 3.5, 'Just My Luck': 3.0,
    'The Night Listener': 4.5, 'Superman Returns': 4.0,
    'You, Me and Dupree': 2.5},
    'Mick LaSalle':{'Lady in the Water':3.0, 'Snake on a Plane': 4.0,
    'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 3.0,
    'The Night Listener': 2.0},
    'Jack Mattews':{'Lady in the Water': 3.0, 'Snake on a Plane': 4.0,
    'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snake on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = []
    for item in prefs[person1]:
        if item in prefs[person2]:
            print "Common item: " + item
            si.append(item)

    #if they have no ratings in common, return 0
    if len(si) is 0:
        return 0;

    # Add up the squares of all the differences
    sum_of_squares = 0.0
    for item in si:
        sum_of_squares += pow(prefs[person1][item]-prefs[person2][item], 2)

    return 1/(1+sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    # Gen the list of mutually rated items
    si = []
    for item in prefs[p1]:
        if item in prefs[p2]:
            si.append(item)

    n = len(si)

    if n==0: return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq = sum([prefs[p1][it] for it in si])
    sum2Sq = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate Pearson score
    num = pSum-((sum1*sum2)/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r = num/den
    return r
