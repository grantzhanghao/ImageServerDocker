#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # #directly debug dig metric graph.
    # from api.drawgraphs.dig_metric_graph import draw_dig_metric
    # draw_dig_metric(1517853600000, 'fr', True)

    # #directly debug dig path graph.
    # from api.drawgraphs.dig_path_graph import draw_dig_path
    # draw_dig_path('ES41276', isdebug=True)

    #directly debug bank energy per meter graph.
    # from api.drawgraphs.total_energy_graph import draw_total_energy
    # draw_total_energy()

    # #directly debug total energy per meter graph.
    # from api.drawgraphs.dig_time_graph import draw_dig_time
    # draw_dig_time()

    #directly debug toe energy per meter graph.
    # from api.drawgraphs.toe_energy_graph import draw_toe_energy
    # draw_toe_energy()

    #directly debug toe energy per meter graph.
    # from api.drawgraphs.toe_energy_table_graph import draw_toe_energy_table
    # draw_toe_energy_table()

    #debug upper hoist speed graph.
    from api.drawgraphs.upper_hoist_speed_graph import draw_upper_hoist_speed
    draw_upper_hoist_speed('ES41251','2018-01-13','2018-01-14', 'en', True )

