$(function() {
    // zona segura de ejecucion
    console.log('Holis, estoy en el formulario persona');
    
    
    $('#btncrear').on('click', function(){
        // recuperar los datos del formulario
        const nombres = $('#txtnombres').val();
        const apellidos = $('#txtapellidos').val();
        const ci = $('#txtci').val();
        const direccion = $('#txtdireccion').val();
        
        console.log('nombres = ' + nombres);
        console.log("apellidos = " + apellidos);
        console.log(`cedula ${ci}`);
        console.log(`direccion ${direccion}`);

        if(!nombres.trim()) {
            Swal.fire({
                title: "Error",
                text: "Nombre invalido",
                icon: "error"
            });
            return;
        }
        if(!apellidos.trim()) {
            Swal.fire({
                title: "Error",
                text: "Apellido invalido",
                icon: "error"
            });
            return;
        }
        if(!ci.trim()) {
            Swal.fire({
                title: "Error",
                text: "CI invalido",
                icon: "error"
            });
            return;
        }
        if(!direccion.trim()) {
            Swal.fire({
                title: "Error",
                text: "Direccion invalido",
                icon: "error"
            });
            return;
        }

        // JSON -- Javascript object notation
        const persona = {
            nombres: nombres,
            apellidos: apellidos,
            cedula: ci,
            direccion: direccion
        }
        console.log(persona);

        Swal.fire({
            title: "Exitoso",
            text: "Guardando Formulario",
            icon: "success"
        });
    });
});