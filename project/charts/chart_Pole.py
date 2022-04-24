import altair as alt


def get_chart_overall(data):
    hover = alt.selection_single(
        fields=["Year"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Minimal Pole area of every year")
        .mark_line()
        .encode(
            #x=alt.X("Year",axis=alt.Axis(format='{}')),
            x = "Year",
            #y=alt.Y("Percentage",axis=alt.Axis(format='%')),
            y=alt.Y("Minimal_area",axis=alt.Axis(format='')),
            color=alt.Color("Region",legend=alt.Legend(orient='bottom'),scale=alt.Scale(scheme='dark2')),
            strokeDash="Region",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="Year",
            y="Minimal_area",
            opacity=alt.condition(hover, alt.value(0.75), alt.value(0)),
            tooltip=[
                alt.Tooltip("Year", title="Year"),
                alt.Tooltip("Minimal_area", title="Minimal_area()"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

# ********************************************
def get_chart_north(data):
    hover = alt.selection_single(
        fields=["Month"],
        nearest=True,
        on="mouseover",
        empty="none",
    )
    lines = (
        alt.Chart(data, title="North Pole area of every month")
        .mark_line()
        .encode(
            #x=alt.X("Year",axis=alt.Axis(format='{}')),
            x = "Month",
            #y=alt.Y("Percentage",axis=alt.Axis(format='%')),
            y=alt.Y("area",axis=alt.Axis(format='')),
            color=alt.Color("Year",legend=alt.Legend(orient='bottom'),scale=alt.Scale(scheme='dark2')),
            strokeDash="Year",
        )
    )
    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)
    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="Month",
            y="area",
            opacity=alt.condition(hover, alt.value(0.75), alt.value(0)),
            tooltip=[
                alt.Tooltip("Month", title="Month"),
                alt.Tooltip("area", title="area()"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()

# ********************************************
def get_chart_south(data):
    hover = alt.selection_single(
        fields=["Month"],
        nearest=True,
        on="mouseover",
        empty="none",
    )
    lines = (
        alt.Chart(data, title="South Pole area of every month")
        .mark_line()
        .encode(
            #x=alt.X("Year",axis=alt.Axis(format='{}')),
            x = "Month",
            #y=alt.Y("Percentage",axis=alt.Axis(format='%')),
            y=alt.Y("area",axis=alt.Axis(format='')),
            color=alt.Color("Year",legend=alt.Legend(orient='bottom'),scale=alt.Scale(scheme='dark2')),
            strokeDash="Year",
        )
    )
    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)
    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="Month",
            y="area",
            opacity=alt.condition(hover, alt.value(0.75), alt.value(0)),
            tooltip=[
                alt.Tooltip("Month", title="Month"),
                alt.Tooltip("area", title="area()"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + points + tooltips).interactive()