import { onMounted, onUnmounted, defineAsyncComponent, shallowRef } from "vue";

export function useScreen() {
    const layout = shallowRef();

    const onLayoutResize = () => {
        const width = window.innerWidth;

        if (width < 768) {
            layout.value = defineAsyncComponent(() => import(`../layouts/SmallLayout.vue`));
        } else if (width < 1200) {
            layout.value = defineAsyncComponent(() => import(`../layouts/MediumLayout.vue`));
        } else {
            layout.value = defineAsyncComponent(() => import(`../layouts/LargeLayout.vue`));
        }

    }

    onMounted(() => {
        onLayoutResize();
        window.addEventListener('resize', onLayoutResize);
    })

    onUnmounted(() => {
        window.removeEventListener('resize', onLayoutResize);
    })

    return {
        layout
    }
}