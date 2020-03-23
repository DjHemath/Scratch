let data = [
    {
        letter: "NOVEMBER",
        frequency: "3"
    },
    {
        letter: "JANUARY",
        frequency: "1"
    },
    {
        letter: "SEPTEMBER",
        frequency: "2"
    },
    {
        letter: "OCTOBER",
        frequency: "6"
    },
    {
        letter: "JANUARY",
        frequency: "1"
    }
]

let months = {
    january: 1,
    febrauary: 2,
    march: 3,
    april: 4,
    may: 5,
    june: 6,
    july: 7,
    august: 8,
    september: 9,
    october: 10,
    november: 11,
    december: 12
}

data = data.map(datum =>
{
    datum.month = months[datum.letter.toLowerCase()]
    return datum
})

data.sort(function(a, b)
{
    return a.month - b.month
})

console.log(data)