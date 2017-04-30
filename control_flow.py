#Simple chords snippet
#-------------------------------------
# Original

ct = tf.constant(0) #counter
[_, _, x_sample] = control_flow_ops.while_loop(lambda count, num_iter, *args: count < num_iter,
                                         gibbs_step, [ct, tf.constant(k), x])

# intermediate
ct = tf.constant(0) #counter
cond = lambda count, num_iter, *args: count < num_iter
[_, _, x_sample] = control_flow_ops.while_loop(cond, gibbs_step, [ct, tf.constant(k), x])

# Proposed fix

ct = tf.constant(0)
cond = lambda count, k, x: tf.less(count,k)
[_,_, xSample] = tf.while_loop(cond, gibbs_step, [ct, tf.constant(k), self.x])


#Long chords snippet RBM.py
#-----------------------------------

# Original parameters are While(condition, body, [initial_accumulator])
[_, _, x_sample] = control_flow_ops.While(lambda count, num_iter, *args: count < num_iter,
                                          gibbs_step, [ct, tf.constant(k), x], 1, False)

# while_loop(cond, body, loop_vars, shape_invariants=None, parallel_iterations=10, back_prop=True, swap_memory=False, name=None)

[_, _, x_sample] = tf.while_loop(lambda count, num_iter, *args: count < num_iter, gibbs_step,
                                 [ct, tf.constant(k), x], parallel_iterations=1, back_prop=False)