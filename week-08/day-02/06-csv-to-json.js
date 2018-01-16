const data = `Phasianus colchicus;9442;Fuscia
Pedetes capensis;2869;Puce
Recurvirostra avosetta;4285;Fuscia
Kobus defassa;4726;Red
Anser anser;8163;Violet
Callipepla gambelii;4422;Fuscia
Ara ararauna;7935;Aquamarine
Ara ararauna;3081;Crimson
Pelecanus conspicillatus;9831;Mauv
Cynictis penicillata;839;Puce
Graspus graspus;9814;Indigo
Vicugna vicugna;6439;Violet
Lemur catta;2023;Pink
Tragelaphus scriptus;986;Aquamarine
Corythornis cristata;4995;Red
Sitta canadensis;6786;Puce
Sus scrofa;9338;Goldenrod
Psophia viridis;8881;Yellow
Gabianus pacificus;7714;Aquamarine
Sus scrofa;6449;Orange
Pteropus rufus;5816;Yellow
Macropus agilis;1241;Teal
Pavo cristatus;5860;Violet
Corythornis cristata;5358;Khaki
Loris tardigratus;725;Orange`;

// Convert the above string (which is in CSV format) to an array of objects
// Columns should map to the following object:
//  { name: "Macropus agilis", id: 1241, color_code: "Teal" }

// Remove all duplicates based on their name, always keep the first one
// Don't use for or forEach

// console.log(data.split('\n'));

let result = data
  .split('\n')
  .map(function(item) {
    let values = item.split(';');
    return {
      name: values[0],
      id: Number(values[1]),
      colorCode: values[2]
    };
  })
  .filter(function(item, index, array) {
    return array.map(mapItem => mapItem['name']).indexOf(item['name']) === index;
  });

  console.log(result);
  console.log(result.length);