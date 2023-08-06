# coding=utf-8
# created by msgi on 2020/4/26 7:52 下午

import os
import time
import tensorflow as tf


class BasicRNNGeneration:

    def __init__(self, vocab_size, embedding_dim, batch_size, rnn_units, ):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.batch_size = batch_size
        self.rnn_units = rnn_units

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.embedding_dim,
                                      batch_input_shape=[self.batch_size, None]),
            tf.keras.layers.GRU(self.rnn_units,
                                return_sequences=True,
                                stateful=True,
                                recurrent_initializer='glorot_uniform'),
            tf.keras.layers.Dense(self.vocab_size)
        ])
        return model

    def train_model(self, epochs):
        # 检查点保存至的目录
        checkpoint_dir = './training_checkpoints'

        # 检查点的文件名
        checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

        model = self._build_model()
        optimizer = tf.keras.optimizers.Adam()
        for epoch in range(epochs):
            start = time.time()

            # 在每个训练周期开始时，初始化隐藏状态
            # 隐藏状态最初为 None
            hidden = model.reset_states()

            for (batch_n, (inp, target)) in enumerate(dataset):
                loss = self.train_step(inp, target, model, optimizer)

                if batch_n % 100 == 0:
                    template = 'Epoch {} Batch {} Loss {}'
                    print(template.format(epoch + 1, batch_n, loss))

            # 每 5 个训练周期，保存（检查点）1 次模型
            if (epoch + 1) % 5 == 0:
                model.save_weights(checkpoint_prefix.format(epoch=epoch))

            print('Epoch {} Loss {:.4f}'.format(epoch + 1, loss))
            print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))

        model.save_weights(checkpoint_prefix.format(epoch=epoch))
        return model

    @tf.function
    def train_step(self, inp, target, model, optimizer):
        with tf.GradientTape() as tape:
            predictions = model(inp)
            loss = tf.reduce_mean(
                tf.keras.losses.sparse_categorical_crossentropy(
                    target, predictions, from_logits=True))
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

        return loss

    def generate(self, base_text):
        # 评估步骤（用学习过的模型生成文本）

        # 要生成的字符个数
        num_generate = 1000

        # 将起始字符串转换为数字（向量化）
        input_eval = [self.char2idx[s] for s in base_text]
        input_eval = tf.expand_dims(input_eval, 0)

        # 空字符串用于存储结果
        text_generated = []

        # 低温度会生成更可预测的文本
        # 较高温度会生成更令人惊讶的文本
        # 可以通过试验以找到最好的设定
        temperature = 1.0

        # 这里批大小为 1
        self.model.reset_states()
        for i in range(num_generate):
            predictions = self.model(input_eval)
            # 删除批次的维度
            predictions = tf.squeeze(predictions, 0)

            # 用分类分布预测模型返回的字符
            predictions = predictions / temperature
            predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

            # 把预测字符和前面的隐藏状态一起传递给模型作为下一个输入
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(self.idx2char[predicted_id])

        return base_text + ''.join(text_generated)

    def preprocess(self):
        pass

        path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

