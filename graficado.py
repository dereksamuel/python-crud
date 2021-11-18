from bokeh.plotting import figure, output_file, show


def main():
  output_file("graphic.html")
  fig = figure()

  total_vals = int(input("Do you want display vals..."))
  x_vals = list(range(total_vals))
  y_vals = []

  for x in x_vals:
    val = int(input(f"Value Y for {x} "))
    y_vals.append(val)

  fig.line(x_vals, y_vals, line_width=2)
  show(fig)


if __name__ == "__main__":
  main()

