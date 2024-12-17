<style lang='stylus'>  
.subway-station {   
  cursor: pointer;  
  transition: 0.3;  
  opacity: 0;  

  &.is-show {  
    opacity: 1;  
  }  

  &:hover {  
    stroke: #000;  
  }  
}  
</style>  

<template>
  <svg class="subway-stations" xmlns="http://www.w3.org/2000/svg" viewBox="100 50 1800 1400">
    <g>
      <g v-for="(item, index) in data" :key="index">
        <circle class="subway-station" :class="{ 'is-show': item.show }" :r="calculateRadius(index)" :id="item.name"
          :cx="item.x" :cy="item.y" :fill="getColor(calculateRadius(index))" stroke="none"></circle>
      </g>
    </g>
  </svg>
</template>  

<script>

import inflowData from '~/common/data/beijing-subway-inflows.json';
import outflowData from '~/common/data/beijing-subway-outflows.json';

export default {
  components: {},
  props: {
    data: Array,
    sliderValue: Number,
    isoutflow: Boolean,
  },

  data() {
    return {
      inflows: [],
      outflows: [],
    };
  },

  computed: {},

  mounted() {
    this.loadData();
    console.log("加载");
  },

  watch: {
    sliderValue(newVal, oldVal) {
      if ((newVal / 96) != (oldVal / 96))
        this.loadData();
      // console.log(newVal + " " + oldVal)
    }
  },

  methods: {
    getColor(radius) {
      // 根据半径返回颜色
      const minRadius = 0; // 最小半径
      const maxRadius = 70; // 最大半径
      const normalizedRadius = Math.min(Math.max(radius, minRadius), maxRadius); // 限制半径范围

      // 计算颜色的比例
      const ratio = Math.pow((normalizedRadius - minRadius) / (maxRadius - minRadius), 0.8);

      // 渐变颜色调整：饱和度较低的颜色，从浅黄到浅红
      const red = Math.floor(180 * ratio + 75); // 红色分量，限制最大值到200，增加基础亮度
      const green = Math.floor(200 * (1 - ratio) + 55); // 绿色分量，限制最大值到200，增加基础亮度
      const blue = Math.floor(30 * (1 - ratio)); // 蓝色分量，保持较低范围变化

      return `rgb(${red}, ${green}, ${blue})`; // 返回 RGB 颜色
    },

    calculateRadius(index) {
      const flows = this.isoutflow ? this.outflows : this.inflows;
      const value = flows[this.sliderValue % 96][index];

      // 指数映射  
      const maxValue = 6650; // 最大值  
      const maxRadius = 70; // 最大半径  

      // 计算半径，使用平方根减缓增长速度  
      const mappedRadius = value > 0 ? Math.pow(value / maxValue, 0.8) * maxRadius : 0;

      return mappedRadius; // 返回计算后的半径  
    },
    loadData() {
      // 懒加载 inflows 和 outflows 的特定部分  
      const left = this.sliderValue - (this.sliderValue % 96)
      const right = left + 96 > 1799 ? 1799 : (left + 96)
      this.inflows = inflowData.slice(left, right);
      this.outflows = outflowData.slice(left, right);
    },
  }
}  
</script>