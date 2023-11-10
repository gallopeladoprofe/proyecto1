$(async function() {
    try {
        const respuesta = await axios.get('https://jsonplaceholder.typicode.com/users');
        //console.log(respuesta.data);
    
        const userLst = respuesta.data;
        //console.log('Holis usando jquery');
    
        // Construyendo el contenido para la tabla
        if(!Array.isArray(userLst) || userLst.length === 0) {
            throw new Error("No es un array válido");
        }

        let contenido = "";
        for(const user of userLst) {
            console.log(user);
            contenido += `
                <tr>
                    <th scope="row">${user.id}</th>
                    <td>${user.name}</td>
                    <td>${user.username}</td>
                    <td>${user.email}</td>
                </tr>
            `;
        }
        $('#tbl_users tbody').html(contenido);
        
    } catch (error) {
        console.error(error);
    }
});