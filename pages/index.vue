<template>
  <section class="container">
    <div class="content-wrapper">
      <div class="legend-wrapper">
        <sw-legend>
          <select-lines @update="handleUpdate" :data="lines" :lines="linesData"></select-lines>
          <!-- <el-checkbox-group v-model="showStatus" size="small">
            <el-checkbox label="已建成" border></el-checkbox>
            <el-checkbox label="在建中" border></el-checkbox>
            <el-checkbox label="规划" border></el-checkbox>
          </el-checkbox-group> -->
        </sw-legend>
        <el-slider class="el_slider" :value="sliderValue" :min="0" :max="100" :step="1" show-tooltip @input="updateSliderValue"></el-slider>
        <div>当前半径: {{ sliderValue }}</div>
      </div>
      <div class="subway-wrapper">
        <subway :lines="lines" :stations="stations" :texts="texts" :sliderValue="sliderValue"></subway>
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
      sliderValue: 20 // 初始化 sliderValue  
    }
  },

  mounted() {
    this.lines = arrInit(data.lines)
    this.stations = arrInit(data.stations)
    this.texts = arrInit(data.texts)
  },

  methods: {
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
    }
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