# frozen_string_literal: true

require_relative './one_way'
RSpec.describe 'one way' do
  describe 'both strings have same length' do
    context 'replacement' do
      context 'same string' do
        subject { one_way('make', 'make') }
        it 'returns true' do
          expect(subject).to be_truthy
        end
      end
      context 'one replacement away' do
        subject { one_way('make', 'bake') }
        it 'returns true' do
          expect(subject).to be_truthy
        end
      end

      context 'two replacement away' do
        subject { one_way('make', 'brke') }
        it 'returns true' do
          expect(subject).to be_falsy
        end
      end
    end
    context 'insert' do
      subject { one_way('make', 'makes') }
      it 'returns true' do
        expect(subject).to be_truthy
      end
    end

    context 'requires two inserts' do
        subject { one_way('make', 'makess') }
        it 'returns false' do
          expect(subject).to be_falsy
        end
    end

    context 'delete' do
        subject { one_way('mke', 'make') }
        it 'returns true' do
          expect(subject).to be_truthy
        end
    end
  end

end
