<template>
  <q-layout view="hhh lpR lfr">
    <q-header reveal elevated class="bg-mk text-black header">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left" />

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          Title
        </q-toolbar-title>
        <q-space />
        <q-select
          v-model="namespace"
          :options="namespaces"
          filled
          label="Namespace"
          class="namespace"
        />
        <q-btn flat round dense icon="group_add" />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="left" side="left" persistent bordered>
      <!-- drawer content -->
      <q-list>
        <q-item-label header>Essential Links</q-item-label>
        <q-item clickable tag="a" rel="noopener" to="/overview">
          <q-item-section avatar>
            <q-icon name="school" />
          </q-item-section>
          <q-item-section>
            <q-item-label>概览</q-item-label>
            <q-item-label caption>https://quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item clickable tag="a" rel="noopener" to="/deployments">
          <q-item-section avatar>
            <q-icon name="school" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Deployments</q-item-label>
            <q-item-label caption>https://quasar.dev</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          clickable
          tag="a"
          rel="noopener"
          href="https://github.quasar.dev"
        >
          <q-item-section avatar>
            <q-icon name="code" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Statefulsets</q-item-label>
            <q-item-label caption>github.com/quasarframework</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "MainLayout",
  data() {
    return {
      left: true,
      namespaces: ["all"],
      namespace: "all",
    };
  },
  methods: {
    getNamespaces() {
      this.namespaces = ["all"];
      this.$api
        .get("/api/v1/namespaces")
        .then((res) => {
          res.data.data.forEach((item) => {
            this.namespaces.push(item);
          });
        })
        .catch((err) => {
          this.$q.notify({
            type: "negative",
            message: `Get Namespaces failed. ${err}`,
          });
        });
    },
  },
  mounted() {
    this.getNamespaces();
  },
};
</script>


<style scoped>
.bg-mk {
  background-color: rgba(156, 154, 154, 0.3);
  -webkit-filter: blur(0px);
  -moz-filter: blur(0px);
  -ms-filter: blur(0px);
  -o-filter: blur(0px);
  filter: blur(0px);
}
.namespace {
  width: 150px;
}
</style>