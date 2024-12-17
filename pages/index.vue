<template>
  <section class="container">
    <div class="content-wrapper">
      <div class="legend-wrapper">
        <sw-legend>
          <select-lines @update="handleUpdate" @resetFlows="handleResetFlows" @startSlide="handleStartSlide" :data="lines"
            :lines="linesData"></select-lines>
        </sw-legend>

        <el-slider class="el_slider" :value="sliderValue" :min="0" :max="1800" :step="1" show-tooltip
          v-model="sliderValue"></el-slider>
        <div>当前时间点: {{ sliderValue }}</div>

        <br>
        <el-switch v-model="startSlide" active-text="openSlide" inactive-text="closeSlide"></el-switch>
        <br>
        <el-switch v-model="isoutflow" active-text="outflow" inactive-text="inflow"></el-switch>

        <br>
      </div>

      <div class="subway-wrapper">
        <!-- <subway :lines="lines" :stations="stations" :texts="texts" :sliderValue="sliderValue" :inflows="inflows" :outflows="outflows"></subway> -->
        <subway :lines="lines" :stations="stations" :texts="texts" :sliderValue="sliderValue" :isoutflow="isoutflow"
          :selectedOption="selectedOption">
        </subway>
      </div>
    </div>
  </section>
</template>

<script>
import data from '~/common/data/beijing-subway.json'
import lines from '~/common/data/beijing-subway-lines.json'
import Subway from '~/components/Subway/Subway'
import SwLegend from '~/components/SwLegend/SwLegend'
import SelectLines from '~/components/Select/SelectLines'

function arrInit(arr) {
  arr.forEach(item => {
    item.show = true
  })
  return arr
}

export default {
  components: {
    Subway, SwLegend, SelectLines
  },

  data() {
    return {
      linesData: lines,
      lines: [],
      stations: [],
      texts: [],
      showStatus: [],

      inflows: [],
      outflows: [],
      sliderValue: 0, // 初始化 sliderValue  
      isoutflow: false, // 初始化开关
      selectedOption: 1,

      startSlide: false, // 滑动开关
      intervalId: null, // 定时器 id
    }
  },

  mounted() {
    this.lines = arrInit(data.lines)
    this.stations = arrInit(data.stations)
    this.texts = arrInit(data.texts)
    // this.inflows = inflowData;
    // this.outflows = outflowData;
  },

  watch: {
    startSlide(newValue) {
      if (newValue) {
        this.startAutoSlide(); // 开启自动滑动  
      } else {
        this.stopAutoSlide(); // 关闭自动滑动  
      }
    }
  },

  methods: {
    startAutoSlide() {
      // 每100毫秒更新一次滑动条的值  
      this.intervalId = setInterval(() => {
        if (this.sliderValue < 1800) {
          this.sliderValue += 1; // 增加滑动条的值  
        } else {
          this.sliderValue = 0; // 重置滑动条的值  
        }
      }, 16);
    },
    stopAutoSlide() {
      // 清除定时器  
      clearInterval(this.intervalId);
    },
    handleSelectChange(value) {
      console.log('selectChange 事件被触发，值：', value)
      this.selectedOption = value
    },
    handleResetFlows() {
      this.sliderValue = 0 // 初始化 sliderValue  
      this.isoutflow = false // 初始化开关
      console.log('resetFlows', this.selectedOption)
    },
    updateSliderValue(value) {
      this.sliderValue = value; // 更新 sliderValue  
    },
    handleHover(e) {
      console.log(e)
    },
    handleUpdate(isHiddenStationNames = false) {
      const showLines = new Set()
      const hideStations = new Set()

      // 计算需要显示的线路
      this.lines.forEach(item => {
        if (item.show) showLines.add(item.id)
      })

      // 计算需要隐藏的站点
      lines.forEach(item => {
        const { id, stations } = item
        if (!showLines.has(id)) {
          stations.forEach(item => {
            hideStations.add(item)
          })
        }
      })

      lines.forEach(item => {
        const { id, stations } = item
        if (showLines.has(id)) {
          stations.forEach(item => {
            hideStations.delete(item)
          })
        }
      })


      this.texts.forEach(item => {
        item.show = !isHiddenStationNames
        if (hideStations.has(item.title)) {
          item.show = false
        }
      })


      this.stations.forEach(item => {
        // console.log(item.name)
        item.show = true
        if (hideStations.has(item.name)) {
          item.show = false
        }
      })
    },
  },
  beforeDestroy() {
    // 在组件销毁前清除定时器  
    this.stopAutoSlide();
  }
}
</script>

<style scoped>
.container {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.content-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow-y: auto;
}

.legend-wrapper {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: #fff;
  padding: 10px;
}

.subway-wrapper {
  padding: 10px;
}

.el-slider {
  padding-left: 200px;
  padding-right: 200px;
}
</style>