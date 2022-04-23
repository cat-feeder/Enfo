import altair as alt


def get_chart(data):
    hover = alt.selection_single(
        fields=["Year"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="CO2 Emissions By Country")
        .mark_line()
        .encode(
            x="Year",
            y=alt.Y("Emission",axis=alt.Axis(format='.1e')),
            color=alt.Color("Country",legend=alt.Legend(orient='bottom'),scale=alt.Scale(scheme='dark2')),
            strokeDash="Country",
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
            y="Emission",
            opacity=alt.condition(hover, alt.value(0.75), alt.value(0)),
            tooltip=[
                alt.Tooltip("Year", title="Year"),
                alt.Tooltip("Emission", title="Emission()"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()