<script setup>
import { useScreen } from '../composables/screen';

const { layout } = useScreen();
</script>

<template>
    <component :is="layout" />
</template>