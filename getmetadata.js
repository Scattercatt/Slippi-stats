process.argv.forEach(function (val, index, array) {
    slppath = val;
  });

const { SlippiGame } = require("@slippi/slippi-js");

const game = new SlippiGame(slppath);

const metadata = game.getMetadata();
console.log(JSON.stringify(metadata));