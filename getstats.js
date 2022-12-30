process.argv.forEach(function (val, index, array) {
    slppath = val;
  });

const { SlippiGame } = require("@slippi/slippi-js");

const game = new SlippiGame(slppath);

const stats = game.getStats();
console.log(JSON.stringify(stats));