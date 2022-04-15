<template>
  <div>

    <news0518 />
    <news0516 />
    <news0512 />
    <news0121 />
  </div>
</template>
<<script>
import news0516 from './news/News0516'
import news0518 from './news/News0518'
import news0512 from './news/News0512'
import news0121 from './news/News0121'

export default {
  data() {
    return {
      
    }
  },
  components: {
    news0518,
    news0516,
    news0512,
    news0121
  },
}
</script>
