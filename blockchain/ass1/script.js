//You have to hard code these values
let block = 548896;
let curDifficulty = 7184404942701;
let t = curDifficulty;
const firstBlockOnTargetDay = 548795;
const lastBlockOnTargetDay = 548938;

const getDifficulty = async () => {
  const response = await fetch("https://chain.api.btc.com/v3/block/" + block);
  const d = await response.json();
  return d.data.difficulty;
};

const checkDifficulties = async () => {
  while (curDifficulty === 7184404942701) {
    block -= 10;
    curDifficulty = await getDifficulty();

    console.log("----");
    console.log("Difficulty:" + curDifficulty);
    console.log("Block:" + block);
  }
  console.log("----");
  console.log("DONE");
};

const checkForPreviousBlocksWithHigherDifficulty = async () => {
  while (t <= curDifficulty) {
    curDifficulty = t;
    block -= 10;
    t = await getDifficulty();

    console.log("----");
    console.log("Last difficulty: " + curDifficulty);
    console.log("Difficutlty of current block: " + t);
    console.log("Block: " + block);
  }
  console.log("----");
  console.log("DONE");
};

const getNumberOfLargeInterBlockTimes = async () => {
  let curBlock = firstBlockOnTargetDay;
  let n20mIntervals = 0;
  let n30mIntervals = 0;
  let prevTimeStamp = await getTimestampOfBlock(curBlock);
  curBlock += 1;
  while (curBlock <= lastBlockOnTargetDay) {
    let curTimeStamp = await getTimestampOfBlock(curBlock);
    let interval = curTimeStamp - prevTimeStamp;
    if (interval > 1200) n20mIntervals += 1;
    if (interval > 1800) n30mIntervals += 1;

    console.log("----");
    console.log("Current block: " + curBlock);
    console.log("Current timestamp: " + curTimeStamp);
    console.log("Previous timestamp: " + prevTimeStamp);
    console.log("Interval: " + interval);
    console.log(
      "Current number of intervals greater than 20 minute: " + n20mIntervals
    );
    console.log(
      "Current number of intervals greater than 30 minute: " + n30mIntervals
    );

    curBlock += 1;
    prevTimeStamp = curTimeStamp;
  }
  console.log("----");
  console.log("DONE");
};

const getNumberOf10MinIntervalsWithAtleast3Blocks = async () => {
  let curBlock = firstBlockOnTargetDay;
  let n3BlockOn10mIntervals = 0;
  let prevTimeStamp = await getTimestampOfBlock(curBlock);
  let interval = 0;
  let tenMinCounter = 600;
  let blockCounter = 0;
  curBlock += 1;

  while (curBlock <= lastBlockOnTargetDay) {
    if (tenMinCounter >= 0 && blockCounter >= 3) {
      n3BlockOn10mIntervals += 1;
      tenMinCounter = 600;
      blockCounter = 0;
    } else if (tenMinCounter <= 0) {
      tenMinCounter = 600;
      blockCounter = 0;
    }

    let curTimeStamp = await getTimestampOfBlock(curBlock);
    interval = curTimeStamp - prevTimeStamp;
    blockCounter += 1;
    tenMinCounter = tenMinCounter - interval;

    console.log("----");
    console.log("Block: " + curBlock);
    console.log("Blocks in current interval: " + blockCounter);
    console.log(
      "Current number of 10 minute intervals with atleast 3 blocks: " +
        n3BlockOn10mIntervals
    );
    console.log("Ten minute counter: " + tenMinCounter);

    curBlock += 1;
    prevTimeStamp = curTimeStamp;
  }
  console.log("----");
  console.log("DONE");
};

const getTimestampOfBlock = async (b) => {
  const response = await fetch("https://chain.api.btc.com/v3/block/" + b);
  const d = await response.json();
  return d.data.timestamp;
};

getNumberOf10MinIntervalsWithAtleast3Blocks();
