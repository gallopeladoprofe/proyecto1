// Señor Javascript, vas a ejecutar código siempre y cuando se haya terminado
// la carga del HTML
document.addEventListener('DOMContentLoaded', async function() {
    // zona segura
    //console.log('vista tabla, holis')
    // Uso de promesas
    const respuesta = await axios.get('https://jsonplaceholder.typicode.com/users');
    console.log(respuesta.data);

    let la_data = null;
    la_data = await axios.get('https://jsonplaceholder.typicode.com/posts');
    console.log(la_data.data);
    // axios.get('https://jsonplaceholder.typicode.com/posts')
    //         .then((res) => {
    //             la_data = res.data;
    //             console.log(la_data);
    //         })
    //         .catch((error) => console.error(error));
    //console.log(la_data);

    const personas = await axios.get('/hola')
    console.log(personas.data);
});