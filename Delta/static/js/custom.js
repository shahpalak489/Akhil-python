
   $(function() {
      var Origin_autosuggest  =  [
         "AGP",
         "AUH",
         "ATL",
         "PVR",
         "PEK",
         "DEN",
         "DTW",
         "HER",
         "TPA",
         "SFB",
         "MDW",
         "LOS",
         "FLL",
         "FCO",
         "MLB"
      ];
      $( "#Origin" ).autocomplete({
         source: Origin_autosuggest
      });
   });


   $(function() {
      var destination_autosuggest  =  [
         "AGP",
         "AUH",
         "ATL",
         "PVR",
         "PEK",
         "DEN",
         "DTW",
         "HER",
         "TPA",
         "SFB",
         "MDW",
         "LOS",
         "FLL",
         "FCO",
         "MLB"
      ];
      $( "#destination" ).autocomplete({
         source: destination_autosuggest
      });
   });
