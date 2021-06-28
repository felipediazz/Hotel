$(document).ready(function () {
  $("#example").DataTable({
    language: {
      url: "http://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json",
      searchPanes: {
        clearMessage: 'Limpiar',
        collapse: {0: 'Filtros', _: 'Filtros (%d)'},
      }
    },
    searchPanes: {
      cascadePanes: true,
      dtOpts: {
        searching: false,
      },
      
    },
    buttons: ["searchPanes"],
    dom: "Bfrtip",
  });
});
