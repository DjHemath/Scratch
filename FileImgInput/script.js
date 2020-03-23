// Handler Function for submit event
const submitHandler = (e) =>
{
    e.preventDefault()
    console.log("Form Submitted!")
}

// Handler Function for img onchange event
const onChangeHandler = (e) =>
{
    const imgName = e.target.files[0].name
    const id = e.target.id
    console.log(`Image Name: ${imgName}\nId: ${id}`)
}

// Get all the input elements inside the form
const inputs = document.querySelectorAll('form input')

inputs.forEach(input =>
{
    // If the input field is of type 'file', add the event listener [ onChangeHandler() ]
    if(input.type === "file")
    {
        input.addEventListener('change', onChangeHandler)
    }
})

// Attach submit handler to the form
document.querySelector("#form").addEventListener('submit', submitHandler)