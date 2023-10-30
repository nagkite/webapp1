document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    var sqlQuery = document.querySelector("textarea[name='sql_query']").value;
  
    // Make a POST request to the server to correct the SQL query.
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ "sql_query": sqlQuery }));
  
    // Handle the response from the server.
    xhr.onload = function() {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        document.querySelector("#corrected_sql_query").innerHTML = response.corrected_sql_query;
      } else {
        alert("Error correcting SQL query: " + xhr.statusText);
      }
    };
  });