<!--线路选择框-->
<style lang='stylus'>
.select-lines {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  margin: 0 -5px;
  margin-bottom: 8px;

  .select-lines-item + .select-lines-item {
  }
    &-item { 
      display: flex;
      width: 85px;
      height: 40px;
      text-align: center;
      margin: 5px;
      cursor: pointer;
      opacity: 0.5;
      transition: 0.5s;
      border: 1px solid rgba(0, 0, 0, 0);
      align-items: center;
      padding: 8px;
      font-size: 13px;
      border-radius: 4px;
      font-weight: 600;
      line-height: 1;

    &:hover {
      opacity: 0.7;
    }

    &__badge {
      width: 13px;
      height: 13px;
      border-radius: 100%;
      margin-right: 10px;
    }
  }

  .is-active {
    opacity: 1;
  }
}

.hide-station-names-button {
  width: 100%;
  margin-top: 10px;
  display: flex;
  justify-content: hide-station-names-button;
  padding-left: 5px;
}
</style>


<template>
  <div class="select-lines">
    <!-- <el-tooltip v-for="item in list" :key="item.id" effect="dark" :content="item.tooltip" placement="bottom"> -->
    <div v-for="item in list" :key="item.id">
      <div @click="handleClick(item)" class="select-lines-item" :class="{ 'is-active': item.show }"
        :style="{ 'border-color': item.color }">
        <div class="select-lines-item__badge" :style="{ background: item.color }"></div> <!--彩色圆点-->
        {{ item.name }}
      </div>
    </div>
    <!-- </el-tooltip> -->
    
    <div class="hide-station-names-button">
      <el-button type="primary" @click="hideStationNames">隐藏站名</el-button>
      <el-button type="primary" @click="resetLines">重置线路</el-button>
      <el-button type="primary" @click="resetFlows">重置客流</el-button>
    </div>
  </div>
</template>

<script>
import { LINES_STATUS_DETAIL } from '~/common/const'
export default {
  components: {},

  props: {
    data: Array,
    lines: Array
  },

  data() {
    return {
      LINES_STATUS_DETAIL: LINES_STATUS_DETAIL,
      isHiddenStationNames: false
    }
  },

  computed: {
    list() {
      const list = this.data
      list.forEach(item => {

        const status = this.lines.find(_ => _.id === item.id)['status']
        item.tooltip = LINES_STATUS_DETAIL.find(_ => _.id === status)['name']
      })
      return list
    }
  },

  mounted() {

  },

  // 按下鼠标线路隐藏/显现
  methods: {
    handleClick(item) {
      item.show = !item.show
      this.$emit('update', this.isHiddenStationNames)
    },

    hideStationNames() {
      this.isHiddenStationNames = !this.isHiddenStationNames
      this.$emit('update', this.isHiddenStationNames)
    },

    resetLines() {
      this.isHiddenStationNames = false
      this.list.forEach(item => {
        item.show = true
      })
      this.$emit('update')
    },

    resetFlows() {
      this.$emit('resetFlows')
    }
  }
}
</script>
