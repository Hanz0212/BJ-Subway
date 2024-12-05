<style lang='stylus'>
.subway-station {
  fill: #fff;
  stroke: #333;
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
        <circle class="subway-station" :class="{ 'is-show': item.show }"  :r="sliderValue/3" :id="item.name"
          :cx="item.x" :cy="item.y"></circle>
      </g>
    </g>
  </svg>
</template>

<script>

export default {
  components: {},
  props: {
    data: Array,
    sliderValue: Number,
  },

  data() {
    return {
    }
  },

  computed: {},

  mounted() { },

  methods: {}
}
</script>
