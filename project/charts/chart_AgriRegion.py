import altair as alt


def get_chart(data):
    hover = alt.selection_single(
        fields=["Year"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Agricultural Land By Region")
        .mark_line()
        .encode(
            #x=alt.X("Year",axis=alt.Axis(format='{}')),
            x = "Year",
            #y=alt.Y("Percentage",axis=alt.Axis(format='%')),
            y=alt.Y("Percentage",axis=alt.Axis(format='%')),
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
            y="Percentage",
            opacity=alt.condition(hover, alt.value(0.75), alt.value(0)),
            tooltip=[
                alt.Tooltip("Year", title="Year"),
                alt.Tooltip("Percentage", title="Percentage()"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()