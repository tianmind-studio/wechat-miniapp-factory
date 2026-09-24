const { getRandomTopic } = require('../../utils/mock-data');

const app = getApp();

const levelMap = {
  easy: '简单',
  medium: '中等',
  hard: '困难'
};

Page({
  data: {
    selectedCategory: '',
    currentTopic: null,
    levelText: ''
  },

  onShow() {
    if (app.globalData.currentTopic) {
      this.setData({
        currentTopic: app.globalData.currentTopic,
        selectedCategory: app.globalData.currentTopic.category,
        levelText: levelMap[app.globalData.currentTopic.level] || ''
      });
    }
  },

  selectCategory(e) {
    const category = e.currentTarget.dataset.category;
    this.setData({ selectedCategory: category });
    this.randomTopic();
  },

  randomTopic() {
    const topic = getRandomTopic(this.data.selectedCategory);
    this.setData({
      currentTopic: topic,
      levelText: levelMap[topic.level] || ''
    });
    app.globalData.currentTopic = topic;
  },

  goRoll() {
    if (!this.data.currentTopic) {
      wx.showToast({ title: '请先选择题目', icon: 'none' });
      return;
    }
    wx.navigateTo({ url: '/pages/roll/index' });
  }
});
