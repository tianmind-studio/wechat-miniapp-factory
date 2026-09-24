const app = getApp();

const diceEmojis = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

Page({
  data: {
    result: null,
    diceEmoji: '🎲'
  },

  onLoad() {
    const result = app.globalData.rollResult;
    if (!result) {
      wx.redirectTo({ url: '/pages/topic/index' });
      return;
    }
    this.setData({
      result: result,
      diceEmoji: diceEmojis[result.dice - 1]
    });
  },

  reroll() {
    wx.navigateBack();
  },

  newTopic() {
    app.globalData.currentTopic = null;
    app.globalData.rollResult = null;
    wx.reLaunch({ url: '/pages/topic/index' });
  },

  goHome() {
    app.globalData.currentTopic = null;
    app.globalData.rollResult = null;
    wx.reLaunch({ url: '/pages/topic/index' });
  }
});
