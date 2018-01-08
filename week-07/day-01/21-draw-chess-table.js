// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

for (let i = 0; i < 8; i++) {
    (i % 2 === 0) ? console.log('% '.repeat(4)) : console.log(' ' + '% '.repeat(4));
}
