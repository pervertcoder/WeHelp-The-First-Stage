"use strict";

// Task 1

// (X, Y)
// 悟空(0, 0)
// 丁滿(-1, 4)
// 特南克斯(1, -2)
// 弗利沙(4, -1)
// 辛巴(-3, 3)
// 貝吉塔(-4, -1)

const func1 = function (name) {
  let allMembers = {
    悟空: [0, 0],
    丁滿: [-1, 4],
    特南克斯: [1, -2],
    弗利沙: [4, -1],
    辛巴: [-3, 3],
    貝吉塔: [-4, -1],
  };
  let target = {};
  let result = {};
  const left = {
    悟空: [0, 0],
    特南克斯: [1, -2],
    辛巴: [-3, 3],
    貝吉塔: [-4, -1],
  };
  const right = { 丁滿: [-1, 4], 弗利沙: [4, -1] };

  let targetPosition;
  if (name in allMembers) {
    target[name] = allMembers[name];
    delete allMembers[name];
    targetPosition = target[name];
  }

  for (const [otherName, OtherPosition] of Object.entries(allMembers)) {
    const dx = Math.abs(OtherPosition[0] - targetPosition[0]);
    const dy = Math.abs(OtherPosition[1] - targetPosition[1]);
    const distance = dx + dy;
    result[otherName] = distance; // 跑出所有對象所對應的
  }

  if (!(name in right)) {
    result["丁滿"] = result["丁滿"] + 2;
    result["弗利沙"] = result["弗利沙"] + 2;
  }
  if (!(name in left)) {
    result["辛巴"] = result["辛巴"] + 2;
    result["悟空"] = result["悟空"] + 2;
    result["貝吉塔"] = result["貝吉塔"] + 2;
    result["特南克斯"] = result["特南克斯"] + 2;
  } // 把過斜線距離+2的條件加進去
  //   console.log(result);

  // 找出最大值
  const getAllMaxKey = function () {
    let maxKeyValue = Math.max(...Object.values(result));
    let maxKeys = [];
    for (const [keyMax, valueMax] of Object.entries(result)) {
      if (valueMax === maxKeyValue) {
        maxKeys.push(keyMax);
      }
    }
    return maxKeys.join("、");
  };

  // 找出最小值
  const getAllMinKey = function () {
    let minKeyValue = Math.min(...Object.values(result));
    let minKeys = [];
    for (const [keyMin, valueMin] of Object.entries(result)) {
      if (valueMin === minKeyValue) {
        minKeys.push(keyMin);
      }
    }
    return minKeys.join("、");
  };
  console.log(`最遠${getAllMaxKey()};最近${getAllMinKey()}`);
};

// 範例
func1("辛巴");
console.log("----------");
func1("悟空");
console.log("----------");
func1("弗利沙");
console.log("----------");
func1("特南克斯");
console.log("=========");

// Task 2

// step1:先去判斷criteria的分類，分成'r'跟'c'和名字的，並列出符合這些條件的服務，另外儲存至candidates串列

// step2:計算差值，找出最近的'r'跟'c'，把這些數字儲存在依照差值排序的串列裡面，這個串列叫做sorted_candidates

// step3:接下來是檢查是否有衝突，如果有衝突，就選擇第二好的，這也是為什麼需要做排序

// step4:如果candidates串列只有一個元素，也就是說只有一個服務符合條件，如果此服務衝突，就會回傳Sorry，這是針對那些指名服務的預約

// step5:最後要做紀錄

// criteria:"Field=Value", "Field>=Value", and "Field<=Value"
const services = [
  { name: "S1", r: 4.5, c: 1000 },
  { name: "S2", r: 3, c: 1200 },
  { name: "S3", r: 3.8, c: 800 },
];

let reservationTime = {};
let reservationTime_id = 1;

const criteriaString = function (string) {
  const string1 = Number(string.slice(3));
  return string1;
};

const timeFunction = function (time1, time2) {
  const time = [];
  time.push(time1);
  for (let i = 0; i < time2 - time1; i++) {
    time.push(time[i] + 1);
  }
  return time;
};

const checkTimeConflict = function (time, name = null) {
  const timeSet = new Set(time);

  for (const key in reservationTime) {
    const entries = reservationTime[key];
    const entriesTimeSet = new Set(entries.time);

    const entriesTimeArray = [...entriesTimeSet];

    let hasConflict = false;
    for (const t of entriesTimeSet) {
      if (timeSet.has(t)) {
        hasConflict = true;
        break;
      }
    }
    if (hasConflict) {
      if (name === null || entries.name === name) {
        return entries.name;
      }
    }
  }
  return null;
};

const func2 = function (ss, start, end, criteria) {
  const timeSpread = timeFunction(start, end);
  let candidates = [];

  if (criteria.includes("r<=")) {
    const criteriaCheck = criteriaString(criteria);
    for (const s of ss) {
      if (s["r"] <= criteriaCheck) {
        candidates.push(s);
      }
    }
  }

  if (criteria.includes("r>=")) {
    const criteriaCheck = criteriaString(criteria);
    for (const s of ss) {
      if (s["r"] >= criteriaCheck) {
        candidates.push(s);
      }
    }
  }

  if (criteria.includes("c<=")) {
    const criteriaCheck = criteriaString(criteria);
    for (const s of ss) {
      if (s["c"] <= criteriaCheck) {
        candidates.push(s);
      }
    }
  }

  if (criteria.includes("c>=")) {
    const criteriaCheck = criteriaString(criteria);
    for (const s of ss) {
      if (s["c"] >= criteriaCheck) {
        candidates.push(s);
      }
    }
  }

  if (criteria.includes("name=")) {
    const serName = criteria.slice(4);
    for (const s of ss) {
      if (s["name"] === serName) {
        candidates.push(s);
      }
    }
  }

  let flag = false;
  for (const k of ["r<=", "r>=", "c<=", "c>="]) {
    if (criteria.includes(k)) {
      flag = true;
      break;
    }
  }

  let sortedCandidates = [];
  let key = null;
  if (flag) {
    if (criteria.includes("r")) {
      key = "r";
    } else {
      key = "c";
    }

    const criteriaCheck = criteriaString(criteria);

    let diffs = [];
    for (const s of candidates) {
      diffs.push([Math.abs(s[key] - criteriaCheck), s]);
    }

    diffs.sort((a, b) => a[0] - b[0]);
    for (const item of diffs) {
      sortedCandidates.push(item[1]);
    }
  } else {
    sortedCandidates = candidates;
  }

  for (const s of sortedCandidates) {
    if (!checkTimeConflict(timeSpread, s.name)) {
      reservationTime[reservationTime_id] = {
        name: s.name,
        time: timeSpread,
      };
      reservationTime_id += 1;
      return s.name;
    }
  }
  if (sortedCandidates.length === 1) {
    return "sorry";
  }
  return "sorry";
};

console.log(func2(services, 15, 17, "c>=800")); // S3
console.log(func2(services, 11, 13, "r<=4")); // S3
console.log(func2(services, 10, 12, "name=S3")); // Sorry
console.log(func2(services, 15, 18, "r>=4.5")); // S1
console.log(func2(services, 16, 18, "r>=4")); // Sorry
console.log(func2(services, 13, 17, "name=S1")); // Sorry
console.log(func2(services, 8, 9, "c<=1500")); // S2
console.log(func2(services, 8, 9, "c<=1500")); // S1
console.log("==========");

// Task 3
// 25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17, …
// Find out the nth term in this sequence.

const functionA = function (data) {
  let arrA = [];
  let num = 25;
  let arrCombinedA;
  let arrACopy;
  while (num >= data) {
    arrA.push(num);
    arrACopy = [...arrA];
    arrCombinedA = [...arrA, ...arrACopy];
    num -= 2;
  }
  let arrCombinedAV1 = arrCombinedA.sort((a, b) => b - a);
  arrCombinedAV1.splice(0, 1);
  arrCombinedAV1.push("_");
  let pairsA = [];
  for (let i = 0; i < arrCombinedAV1.length; i += 2) {
    pairsA.push([arrCombinedAV1[i], arrCombinedAV1[i + 1]]);
  }
  return pairsA;
};

const functionB = function (data) {
  let dataB = data - 4;
  let arrB = [];
  let numB = 21;
  while (numB >= dataB) {
    arrB.push(numB);
    numB -= 1;
  }
  arrB.push("_");
  let pairsB = [];
  for (let p = 0; p < arrB.length; p += 2) {
    pairsB.push([arrB[p + 1], arrB[p]]);
  }
  return pairsB;
};
const sequence = function (dataA) {
  let dataB = dataA - 4;
  let resultArrA = functionA(dataA);
  let resultArrB = functionB(dataB);

  let newList = [];
  for (let i = 0; i < resultArrA.length; i++) {
    newList.push(resultArrA[i]);
    newList.push(resultArrB[i]);
  }
  // return newList;
  let newList2 = [];
  for (let i = 0; i < newList.length; i++) {
    for (let j = 0; j < newList[i].length; j++) {
      newList2.push(newList[i][j]);
    }
  }
  return newList2;
};
const ans = sequence(-1000);
const func3 = function (index) {
  return ans[index];
};
//資料量一大就跑超級慢><
// 範例
console.log(func3(1));
console.log(func3(5));
console.log(func3(10));
console.log(func3(30));
console.log("=========");

// Task 4

// - Available Spaces: list/array containing number of available seats for each car.
// - Status Bitmap: string containing only 0 or 1. 0 means the corresponding car can
// serve passengers for now.
// - Passenger Number: number of incoming passengers

const func4 = function (sp, stat, n) {
  const statArray = [...stat];
  let check = [];
  for (let i = 0; i < sp.length; i++) {
    if (Number(statArray[i]) === 1) {
      sp[i] = "_";
    } else {
      sp[i] = Math.abs(sp[i] - n);
      check.push(sp[i]);
    }
  }
  let vacancy = Math.min(...check);
  let vacancyCheck = sp.indexOf(vacancy);
  return vacancyCheck;
};

// 範例
console.log(func4([3, 1, 5, 4, 3, 2], "101000", 2)); // 5
console.log(func4([1, 0, 5, 1, 3], "10100", 4)); // 4
console.log(func4([4, 6, 5, 8], "1000", 4)); // 2
