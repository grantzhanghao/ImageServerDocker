#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangorest.settings")
    try:
        from django.core.management import execute_from_command_line

        # #debug dig metric graph
        # from api.views.dig_metric_view import DigMetricView
        # graph = DigMetricView()
        # url = 'http://127.0.0.1:8000/get_dig_metric_graph?shift_start_timestamp=1517853600000&locale=ch'
        # graph.debug_graph(url)

        # #debug dig path graph
        # from api.views.dig_path_view import DigPathView
        # graph = DigPathView()
        # url = 'http://127.0.0.1:8000/get_dig_path_graph?equipment=ES41276&locale=fr'
        # graph.debug_graph(url)

        #debug toe energy graph
        # from api.views.toe_energy_view import ToeEnergyView
        # graph = ToeEnergyView()
        # url = 'http://127.0.0.1:8000/get_toe_energy_graph?phserialno=ES41251&start_time=2018-2-1&locale=ch'
        # graph.debug_graph(url)

        # debug total energy graph
        # from api.views.total_energy_view import TotalEnergyView
        # graph = TotalEnergyView()
        # url = 'http://127.0.0.1:8000/get_total_energy_graph?phserialno=ES41251&start_time=2018-2-1&locale=ch'
        # graph.debug_graph(url)

        # debug dig time graph
        # from api.views.dig_time_view import DigTimeView
        # graph = DigTimeView()
        # url = 'http://127.0.0.1:8000/get_dig_time_graph?phserialno=ES41251&start_time=2018-2-1&locale=ch'
        # graph.debug_graph(url)

        # debug upper hoist speed graph
        # from api.views.upper_hoist_speed_view import UpperHoistSpeedView
        # graph = UpperHoistSpeedView()
        # url = 'http://127.0.0.1:8000/get_upper_hoist_speed_graph?phserialno=ES41251&start_time=2018-2-1&locale=ch'
        # graph.debug_graph(url)

        # debug upper hoist speed graph
        from api.views.mock_picture_view import MockPicture
        graph = MockPicture()
        url = 'http://127.0.0.1:8000/get_mock_graph'
        graph.debug_graph(url)
    except ImportError as exc:
        print(exc)
