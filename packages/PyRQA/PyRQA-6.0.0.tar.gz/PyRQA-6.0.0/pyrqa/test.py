#!/usr/bin/env python

"""
Run all tests of the project.
"""

import unittest

__author__ = "Tobias Rawald"
__copyright__ = "Copyright 2015-2020 The PyRQA project"
__credits__ = ["Tobias Rawald",
               "Mike Sips"]
__license__ = "Apache-2.0"
__maintainer__ = "Tobias Rawald"
__email__ = "pyrqa@gmx.net"
__status__ = "Development"


if __name__ == "__main__":
    loader = unittest.TestLoader()

    print("""\n
Recurrence Plot Tests
=====================
""")

    recurrence_plot_suite = unittest.TestSuite()
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.RPClassicFixedRadiusTestCase'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.RPClassicRadiusCorridorTestCase'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.RPCrossFixedRadiusTestCase'))
    recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.radius.test.RPCrossRadiusCorridorTestCase'))

    unittest.TextTestRunner(verbosity=2).run(recurrence_plot_suite)

    print("""\n
Unthresholded Recurrence Plot Tests
===================================
""")

    unthresholded_recurrence_plot_suite = unittest.TestSuite()
    unthresholded_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.unthresholded.test.RPClassicUnthresholdedTestCase'))
    unthresholded_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rp.unthresholded.test.RPCrossUnthresholdedTestCase'))


    unittest.TextTestRunner(verbosity=2).run(unthresholded_recurrence_plot_suite)

    print("""\n
Joint Recurrence Plot Tests
===========================
""")

    joint_recurrence_plot_suite = unittest.TestSuite()
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicClassicFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicClassicFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicClassicRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicClassicRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicCrossFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicCrossFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicCrossRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPClassicCrossRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossClassicFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossClassicFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossClassicRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossClassicRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossCrossFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossCrossFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossCrossRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_plot_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrp.test.JRPCrossCrossRadiusCorridorRadiusCorridorTestCase'))

    unittest.TextTestRunner(verbosity=2).run(joint_recurrence_plot_suite)

    print("""\n
Recurrence Quantification Analysis Tests
========================================
""")

    recurrence_quantification_analysis_suite = unittest.TestSuite()
    recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.RQAClassicFixedRadiusTestCase'))
    recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.RQAClassicRadiusCorridorTestCase'))
    recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.RQACrossFixedRadiusTestCase'))
    recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.rqa.radius.test.RQACrossRadiusCorridorTestCase'))

    unittest.TextTestRunner(verbosity=2).run(recurrence_quantification_analysis_suite)

    print("""\n
Joint Recurrence Quantification Analysis Tests
==============================================
""")

    joint_recurrence_quantification_analysis_suite = unittest.TestSuite()

    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicClassicFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicClassicFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicClassicRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicClassicRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicCrossFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicCrossFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicCrossRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQAClassicCrossRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossClassicFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossClassicFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossClassicRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossClassicRadiusCorridorRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossCrossFixedRadiusFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossCrossFixedRadiusRadiusCorridorTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossCrossRadiusCorridorFixedRadiusTestCase'))
    joint_recurrence_quantification_analysis_suite.addTests(
        loader.loadTestsFromName('pyrqa.variants.jrqa.test.JRQACrossCrossRadiusCorridorRadiusCorridorTestCase'))

    unittest.TextTestRunner(verbosity=2).run(joint_recurrence_quantification_analysis_suite)
