/**
 * 骰盅组局 mock 数据
 * 所有题目和玩家都是示例数据，正式使用前请替换
 */

const topics = [
  {
    id: 'truth-1',
    category: '真心话',
    text: '你最近一次说谎是什么时候？',
    level: 'easy'
  },
  {
    id: 'truth-2',
    category: '真心话',
    text: '你手机里最不想让别人看到的 app 是哪个？',
    level: 'medium'
  },
  {
    id: 'truth-3',
    category: '真心话',
    text: '你觉得在场谁最可能成为明星？',
    level: 'easy'
  },
  {
    id: 'dare-1',
    category: '大冒险',
    text: '模仿一个在场的人说话 30 秒',
    level: 'medium'
  },
  {
    id: 'dare-2',
    category: '大冒险',
    text: '给你通讯录里最近联系的人发一条"我想你了"',
    level: 'hard'
  },
  {
    id: 'dare-3',
    category: '大冒险',
    text: '用方言说一段绕口令',
    level: 'easy'
  },
  {
    id: 'who-1',
    category: '谁最可能',
    text: '谁最可能在凌晨三点还在刷手机？',
    level: 'easy'
  },
  {
    id: 'who-2',
    category: '谁最可能',
    text: '谁最可能一个人去旅行？',
    level: 'easy'
  },
  {
    id: 'who-3',
    category: '谁最可能',
    text: '谁最可能成为创业老板？',
    level: 'easy'
  }
];

const defaultPlayers = [
  { id: 'p1', name: '玩家 A', avatar: '🎲' },
  { id: 'p2', name: '玩家 B', avatar: '🎯' },
  { id: 'p3', name: '玩家 C', avatar: '🎪' },
  { id: 'p4', name: '玩家 D', avatar: '🎨' }
];

function getRandomTopic(category) {
  const filtered = category 
    ? topics.filter(t => t.category === category)
    : topics;
  return filtered[Math.floor(Math.random() * filtered.length)];
}

function getRandomPlayer(players) {
  const list = players && players.length > 0 ? players : defaultPlayers;
  return list[Math.floor(Math.random() * list.length)];
}

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

module.exports = {
  topics,
  defaultPlayers,
  getRandomTopic,
  getRandomPlayer,
  rollDice
};
