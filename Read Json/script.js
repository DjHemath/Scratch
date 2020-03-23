fetch("./read.json")
.then(res => res.json())
.then(data =>
{
    data.forEach(datum =>
    {
        console.log(datum)
    })
})