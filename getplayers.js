process.argv.forEach(function (val, index, array) {
    slppath = val;
  });

const { SlippiGame } = require("@slippi/slippi-js");

const game = new SlippiGame(slppath);

const settings = game.getSettings().players;
console.log(JSON.stringify(settings));
