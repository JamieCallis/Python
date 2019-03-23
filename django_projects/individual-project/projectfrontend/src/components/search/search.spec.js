import { shallowMount } from '@vue/test-utils'
import flushPromises from 'flush-promises'
import search from '@/components/search.vue'
jest.mock('axios')

describe('searchComponent', () => {
    // we are using a shallowMount over Mount the reason for this
    // is a shallowMount only uses the component not it's children components. 
    
    // we need to test if a method prints a the value from search box.
    // we could do an initial test that on click on the search button it prints a statement to the console?
    it('does the data update when you input information into the input?', () => {
        const wrapper = shallowMount(search)
        const input = wrapper.find('input')
        input.setValue('Hello World')
        expect(wrapper.vm.query).toBe('Hello World')
    })

    it('AJAX request to backend', done => {
        const wrapper = shallowMount(search)
        const input = wrapper.find('input')
        input.setValue('European authorities fined Google a record $5.1 billion on Wednesday\
        for abusing its power in the mobile phone market and ordered the company to alter its practices.')
        const button = wrapper.find('button').trigger('click')
        
        wrapper.vm.$nextTick(() => {
            expect(wrapper.vm.queryResult).not.toBe({})
            done()
        })
      
    })

})