// Get HTML elements
let searchInput = document.getElementById('search_box');
let searchResults = document.getElementById('search-results');
let searchTypeahead = document.getElementById('search-typeahead');
let navbar = document.getElementsByClassName('navbar-dark')[0];
console.log(navbar);

// Add event listeners
searchInput.addEventListener('keyup', getSearchResults);

// Function for retrieving the csrf token cookie
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// Assign the csrf token to a variable so it can be used in the AJAX
var csrftoken = getCookie('csrftoken');

function getSearchResults() {
    let xhr = new XMLHttpRequest();
    let searchText = searchInput.value;
    console.log(searchText);
    xhr.onload = function() {
        if (this.readyState == 4 && this.status == 200) {
            let results = JSON.parse(xhr.responseText);
            console.log(results);
            if (searchResults) {
                searchResults.innerHTML = '';
            }
            
            // Loop through the list of dictionaries
            for (var i = 0; i < results.length; i++) {
                
                // Get title and slug from list of dictionaries
                let title =  Object.keys(results[i]);
                let slug = Object.values(results[i]);
                
                // Create the li element
                let li = document.createElement('li');
                li.style.paddingBottom = '10px';
                li.style.paddingLeft = '10px';
                li.setAttribute('id', slug);
                
                // Create link for search result product
                let linkTag = document.createElement('a');
                linkTag.href = "/shoppingcart/product/" + slug;
                linkTag.style.color = 'black';
                
                
                // Add mouse enter and mouse out event listeners for li and link
                li.addEventListener('mouseenter', function() {
                    li.style.backgroundColor = '#929fba';
                });
                
                li.addEventListener('mouseout', function() {
                    li.style.backgroundColor = 'white';
                });
                
                linkTag.addEventListener('mouseenter', function() {
                    li.style.backgroundColor = '#929fba';
                });
                
                linkTag.addEventListener('mouseout', function() {
                    li.style.backgroundColor = 'white';
                });
                
                // Append title as text node to link
                linkTag.appendChild(document.createTextNode(title));
                
                // Append link to li and li to search results
                li.appendChild(linkTag);
                searchResults.appendChild(li);
            }
            searchTypeahead.style.border = '1px solid grey';
            searchTypeahead.style.borderTop = 'none';
            navbar.classList.remove('mb-5');
        }
        xhr.onerror = function() {
            console.log('Request error...');
        };
    };
    xhr.open("POST", "/shoppingcart/search_results/" + searchText + "/", true);
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.send();
}

