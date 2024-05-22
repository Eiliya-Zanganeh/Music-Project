import { configure, defineRule, ErrorMessage, Field, Form } from 'vee-validate'
import {
  alpha_spaces,
  confirmed,
  email,
  max,
  max_value,
  min,
  min_value,
  not_one_of,
  required
} from '@vee-validate/rules'

export default {
  install(app) {
    app.component('VeeForm', Form)
    app.component('VeeField', Field)
    app.component('VeeErrorMessage', ErrorMessage)

    defineRule('required', required)
    defineRule('min', min)
    defineRule('max', max)
    defineRule('alpha_spaces', alpha_spaces)
    defineRule('email', email)
    defineRule('min_value', min_value)
    defineRule('max_value', max_value)
    defineRule('confirmed', confirmed)
    defineRule('not_one_of', not_one_of)

    configure({
      generateMessage: (context) => {
        const messages = {
          required: `The field ${context.field} is required.`,
          min: `The field ${context.field} is too short.`,
          max: `The field ${context.field} is too long.`,
          alpha_spaces: `The field ${context.field} may only contain alphabetical characters and spaces.`,
          email: `The field ${context.field} must be a valid email.`,
          min_value: `The field ${context.field} is too low.`,
          max_value: `The field ${context.field} is too high.`,
          confirmed: "The passwords don't match.",
          not_one_of: `You are not allowed to use this value for the field ${context.field}.`,
        }

        return messages[context.rule.name] ? messages[context.rule.name] : 'اشتباه وارد کردی دا دا'
      },
      validateOnBlur: true,
      validateOnChange: true,
      validateOnInput: true,
      validateOnModelUpdate: true
    })
  }
}