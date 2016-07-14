function sortLibrary() {
  // var library is defined, use it in your code
  // use console.log(library) to output the sorted library data
 function predicatBy(prop){
   return function(a,b){
      if( a[prop] > b[prop]){
          return 1;
      }else if( a[prop] < b[prop] ){
          return -1;
      }
      return 0;
   }
}
console.log(library.sort(predicatBy("title")));
}

// tail starts here
var library = [{
  author: 'Bill Gates',
  title: 'The Road Ahead',
  libraryID: 1254
}, {
  author: 'Steve Jobs',
  title: 'Walter Isaacson',
  libraryID: 4264
}, {
  author: 'Suzanne Collins',
  title: 'Mockingjay: The Final Book of The Hunger Games',
  libraryID: 3245
}];

sortLibrary();
