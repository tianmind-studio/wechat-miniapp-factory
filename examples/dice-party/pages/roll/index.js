const { defaultPlayers, rollDice } = require('../../utils/mock-data');

const app = getApp();

const diceEmojis = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

Page({
  data: {
    currentTopic: null,
    players: defaultPlayers,
    selectedPlayer: null,
    rolling: false,
    diceDisplay: '🎲'
  },

  onLoad() {
    const topic = app.globalData.currentTopic;
    if (!topic) {
      wx.redirectTo({ url: '/pages/topic/index' });
      return;
    }
    this.setData({ currentTopic: topic });
  },

  rollDice() {
    if (this.data.rolling) return;

    this.setData({ rolling: true, selectedPlayer: null });
    
    let count = 0;
    const maxCount = 15;
    
    const interval = setInterval(() => {
      const randomDice = rollDice();
      this.setData({ diceDisplay: diceEmojis[randomDice - 1] });
      count++;
      
      if (count >= maxCount) {
        clearInterval(interval);
        this.finishRoll();
      }
    }, 100);
  },

  finishRoll() {
    const finalDice = rollDice();
    const playerIndex = (finalDice - 1) % this.data.players.length;
    const selectedPlayer = this.data.players[playerIndex];
    
    this.setData({
      rolling: false,
      diceDisplay: diceEmojis[finalDice - 1],
      selectedPlayer: selectedPlayer
    });

    app.globalData.rollResult = {
      dice: finalDice,
      player: selectedPlayer,
      topic: this.data.currentTopic
    };

    setTimeout(() => {
      wx.navigateTo({ url: '/pages/result/index' });
    }, 800);
  }
});
