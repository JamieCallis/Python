import { mount } from '@vue/test-utils'
import search from '@/components/search.vue'


describe('search', () => {
    const wrapper = mount(search)
    it('renders a form element', () => {
        expect(wrapper.contains('form')).toBe(true)
    })

    it('renders a input inside the form', () => {
        // first we find the element
        expect(wrapper.contains('input')).toBe(true)
    })

    it('renders a button inside the ', () => {
        // first we will find the element
        expect(wrapper.contains('button')).toBe(true)
    })
})