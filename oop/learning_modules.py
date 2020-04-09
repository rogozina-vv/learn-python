import input_data
import display_figure
import crossing_check

def main():
    input_data.data_entry()
    n = len(input_data.set_of_shapes)
    display_figure.drawing_shapes(input_data.set_of_shapes, n)
    crossing_check.test_of_shapes(input_data.set_of_shapes, n)

main()