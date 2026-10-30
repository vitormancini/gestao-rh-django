async function utilizarHoraExtra(pk) {
    const response = await window.ajax.post(`/horas-extras/utilizou-hora-extra/${pk}/`);
    console.log(response);
}