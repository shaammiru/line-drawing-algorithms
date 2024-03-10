import re
import pandas as pd
import streamlit as st
from algorithm.dda import dda_algorithm as dda
from algorithm.bresenham import bres_algorithm as bres


def validate_input(input: str):
    pattern = r"^[-+]?\d+,\s*[-+]?\d+$"
    return bool(re.match(pattern, input))


def dda_page():
    st.header("Digital Differential Analyzer (DDA) Algorithm", divider="red")

    start = st.text_input("Enter x0 and y0 (format: x0, y0)")
    end = st.text_input("Enter x1 and y1 (format: x1, y1)")

    cal_btn = st.button("Calculate")

    if cal_btn:
        if start == "" or end == "":
            st.warning("Please enter the coors.")
            return

        if not validate_input(start) or not validate_input(end):
            st.warning("Invalid input format. Please enter in the format x, y.")
            return

        start = start.split(",")
        end = end.split(",")
        start = [int(i) for i in start]
        end = [int(i) for i in end]
        result = dda(start[0], start[1], end[0], end[1])

        data = pd.DataFrame(
            {
                "∆x": [result["dx"]],
                "Δy": [result["dy"]],
                "Step": [result["steps"]],
                "X Increment": [result["x_increment"]],
                "Y Increment": [result["y_increment"]],
            },
            columns=["∆x", "Δy", "Step", "X Increment", "Y Increment"],
        )

        round_x = [i["x"] for i in result["rounded_coor"]]
        round_y = [i["y"] for i in result["rounded_coor"]]
        formatted_xy = [f"({i[0]}, {i[1]})" for i in list(zip(round_x, round_y))]

        coors = pd.DataFrame(
            {
                "X": [i["x"] for i in result["coor"]],
                "Y": [i["y"] for i in result["coor"]],
                "round(X, Y)": formatted_xy,
            },
            columns=["X", "Y", "round(X, Y)"],
        )

        st.subheader("Result")
        st.dataframe(data)
        st.subheader("Coors")
        st.dataframe(coors)


def bresenham_page():
    st.header("Bresenham's Line Algorithm", divider="red")
    start = st.text_input("Enter x0 and y0 (format: x0, y0)")
    end = st.text_input("Enter x1 and y1 (format: x1, y1)")
    cal_btn = st.button("Calculate")

    if cal_btn:
        if start == "" or end == "":
            st.warning("Please enter the coors.")
            return

        if not validate_input(start) or not validate_input(end):
            st.warning("Invalid input format. Please enter in the format x, y.")
            return

        start = start.split(",")
        end = end.split(",")
        start = [int(i) for i in start]
        end = [int(i) for i in end]
        result = bres(start[0], start[1], end[0], end[1])

        st.subheader("Result")

        is_swapped = "Yes" if result["is_swapped"] else "No"
        x_coors = [i["x"] for i in result["coor"]]
        y_coors = [i["y"] for i in result["coor"]]
        format_xy = [f"({i[0]}, {i[1]})" for i in list(zip(x_coors, y_coors))]

        data = pd.DataFrame(
            {
                "∆x": [result["dx"]],
                "Δy": [result["dy"]],
                "Step X": [result["stepX"]],
                "Step Y": [result["stepY"]],
                "P0": [result["p0"]],
                "Is Swapped": [is_swapped],
            }
        )

        coors = pd.DataFrame(
            {
                "P": result["ps"],
                "(X,Y)": format_xy,
            },
            columns=["P", "(X,Y)"],
        )

        if result["is_swapped"]:
            st.write("Swapped x and y coors due to Δy > ∆x.")

            data = pd.DataFrame(
                {
                    "∆x": [result["dy"]],
                    "Δy": [result["dx"]],
                    "Step X": [result["stepY"]],
                    "Step Y": [result["stepX"]],
                    "P0": [result["p0"]],
                    "Is Swapped": [is_swapped],
                }
            )

            x_coors = [i["y"] for i in result["coor"]]
            y_coors = [i["x"] for i in result["coor"]]
            format_swap_xy = [f"({i[0]}, {i[1]})" for i in list(zip(x_coors, y_coors))]

            coors = pd.DataFrame(
                {
                    "P": result["ps"],
                    "(X,Y)": format_xy,
                    "swap(X, Y)": format_swap_xy,
                },
                columns=["P", "(X,Y)", "swap(X, Y)"],
            )

        st.dataframe(data)
        st.subheader("Coors")
        st.dataframe(coors)


def main():
    st.set_page_config(page_title="Shaam | Line Drawing Algorithms")
    st.sidebar.title("Line Drawing Algorithms")
    algorithm = st.sidebar.radio("Select an algorithm", ("DDA", "Bresenham"))

    if algorithm == "DDA":
        dda_page()
    elif algorithm == "Bresenham":
        bresenham_page()

    footer_md = """
    ---
    Made with ☕ by [Shaam](https://github.com/shaammiru).
    
    Give a ⭐ to [my repo](https://github.com/shaammiru/py-dda-bresenham) if you found this helpful.
    """

    st.markdown(footer_md, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
