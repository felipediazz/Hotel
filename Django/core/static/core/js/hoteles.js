$(document).ready(function(){
    $('#example').DataTable({
            searchPanes:{
                cascadePanes:true,
                dtOpts:{
                    searching:false
                }
            },
            dom:'Pfrtip',
            
    });

});

