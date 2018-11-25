<template>
  <div id="drawer" class="drawer">
    <div class="drawer__summary">
      <h1>London Plane</h1>
      <div class="drawer__subtitle">
        <span>Platanus x hispanica</span>
      </div>
      <ul>
        <li>Height 5.76m</li>
        <li>Girth 87cm</li>
        <li>Age ~240</li>
      </ul>
    </div>
    <hr />
    <div class="drawer__about">
      <h2>Special information about this specimen</h2>
      <p>
        London Planes grow very rapidly, and this vast specimen was probably associated with Brislington House. It now fills the valley of the brook, and is hollow. It was in danger of being ruined by fires built inside its hollow trunk, a common fate of veteran trees, but was recently saved by being bricked up. The species came to Britain in 1690, and is still being widely planted.
      </p>
      <hr />
      <h2>General information about this species</h2>
      <p>
        Platanus × acerifolia, the London plane, London planetree, or hybrid plane, is a tree in the genus Platanus. It is often known by the synonym Platanus × hispanica. It is usually thought to be a hybrid of Platanus orientalis (oriental plane) and Platanus occidentalis (American sycamore). Some authorities think that it may be a cultivar of P. orientalis.
      </p>
      <span class="drawer__source">
        Source: Wikipedia
      </span>
      <hr />
      <div class="drawer__report">
        <a target="_blank" href="https://www.bristol.gov.uk/museums-parks-sports-culture/what-to-do-if-you-have-a-problem-with-a-tree">
          Report an issue with this tree <Chevron />
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import Chevron from './Chevron.vue'

export default {
  name: 'treeDrawer',
  data: () => {
    return {
      el: '#drawer',
    }
  },
  components: {
    Chevron
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.drawer {
  background: #fff;
  box-shadow: 0 2px 4px;
  left: 0;
  bottom: 0;
  position: fixed;
  transition: all .5s ease;
  height: 50%;
  overflow-y: scroll;
  padding: 16px;

  &.expanded {
    height: 40px;
  }

  &__button {
    background-color: none;
    border: none;
    cursor: pointer;
    width: 100%;

    &:focus {
      outline: none;
    }
  }

  &__subtitle {
    margin-bottom: 16px;
  }

  &__summary {
    padding-bottom: 16px;
    text-align: left;
  }

  &__about {
    padding-top: 8px;
    text-align: left;
  }

  &__report {
    padding: 8px 0;
    a {
      color: #058E3F;
      font-family: 'Helvetica';
      text-decoration: none;
    }
  }

  &__trees {
    display: flex;
  }

  &__tree {
    text-align: left;
    width: 50%;
  }

  &__source {
    color: grey;
  }
}

h1, h2 {
  color: #058E3F;
  font-family: 'Helvetica';
  font-weight: 400;
  margin: 4px 0;
}

h2 {
  font-size: 18px;
}

hr {
  border: 1px solid;
  color: #EBEBEC;
}

ul {
  list-style-type: none;
  display: inline;
  padding-inline-start: 0;
}

li {
  display: inline;
  position: relative;

  &:not(:first-child) {
    padding-left: 18px;

    &:after {
      background-color: #4F6272;
      content: '';
      display: inline-block;
      border-radius: 20px;
      height: 6px;
      width: 6px;
      position: absolute;
      left: 6px;
      top: 8px;
    }
  }
}
</style>
